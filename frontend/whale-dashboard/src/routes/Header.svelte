<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/bitcoin-btc-logo.svg';
	import github from '$lib/images/github.svg';
</script>

<header>
	<div class="corner">
		<a href="https://kit.svelte.dev">
			<img src={logo} alt="Bitcoin" />
		</a>
	</div>

	<nav>
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/glossary' ? 'page' : undefined}>
				<a href="/glossary">Glossary</a>
			</li>
			<li aria-current={$page.url.pathname.startsWith('/sverdle') ? 'page' : undefined}>
				<a href="/sverdle">Sverdle</a>
			</li>
		</ul>
	</nav>

	<div class="corner">
		<a href="https://github.com/sveltejs/kit">
			<img src={github} alt="GitHub" />
		</a>
	</div>
</header>

<style>
	header {
		@apply flex justify-between;
		@apply bg-white;
		@apply shadow-md;
	}

	.corner {
		@apply w-12;
		@appy h-12;
	}

	.corner a {
		@apply flex items-center;
		@apply justify-center;
		@apply w-full;
		@apply h-full;
	}

	.corner img {
		@apply w-8;
		@apply h-8;
		@apply object-contain;
	}

	nav {
		@apply flex justify-center;
	}

	ul {
		@apply relative;
		@apply p-0;
		@apply m-0;
		@apply h-12;
		@apply flex;
		@apply justify-center;
		@apply items-center;
		@apply list-none;
		@apply bg-[var(--background)];
		@apply bg-contain;
	}

	li {
		@apply relative h-full;
	}

/* Styles for li[aria-current='page']::before */
	li[aria-current='page']::before {
		--size: 6px;
		content: '';
		@apply w-0 h-0 absolute top-0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--color-theme-1);
	}

/* Styles for nav a */
	nav a {
		@apply flex h-full items-center px-2 text-[var(--color-text)] font-bold text-xs uppercase tracking-wider no-underline transition-colors duration-200;
	}

/* Styles for a:hover */
	a:hover {
		@apply text-[var(--color-theme-1)];
	}
</style>
