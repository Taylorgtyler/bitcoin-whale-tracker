// internal/server/routes.go

package server

import (
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

func (s *Server) RegisterRoutes() http.Handler {
    r := chi.NewRouter()
    r.Use(middleware.Logger)

    r.Get("/", s.HelloWorldHandler)
    r.Get("/api/whale-transaction/largest-this-week", s.getLargestWhaleTransactionThisWeek)
    r.Get("/api/whale-transactions/recent", s.getRecentWhaleTransactions)

    return r
}

func (s *Server) HelloWorldHandler(w http.ResponseWriter, r *http.Request) {
    resp := make(map[string]string)
    resp["message"] = "Hello World"

    jsonResp, err := json.Marshal(resp)
    if err != nil {
        http.Error(w, "Failed to create response", http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    w.Write(jsonResp)
}

func (s *Server) getLargestWhaleTransactionThisWeek(w http.ResponseWriter, r *http.Request) {
    transaction, err := s.db.GetLargestWhaleTransactionThisWeek()
    if err != nil {
        http.Error(w, "Failed to fetch whale transaction", http.StatusInternalServerError)
        return
    }

    if transaction == nil {
        http.Error(w, "No whale transactions found this week", http.StatusNotFound)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(transaction)
}

func (s *Server) getRecentWhaleTransactions(w http.ResponseWriter, r *http.Request) {
    limitStr := r.URL.Query().Get("limit")
    limit, err := strconv.Atoi(limitStr)
    if err != nil || limit <= 0 {
        limit = 10 // Default limit
    }

    transactions, err := s.db.GetRecentWhaleTransactions(limit)
    if err != nil {
        http.Error(w, "Failed to fetch whale transactions", http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(transactions)
}