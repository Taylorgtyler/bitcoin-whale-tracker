package database

import (
	"database/sql"

	_ "github.com/marcboeker/go-duckdb"
)

type DBContext struct {
	DB *sql.DB
}

