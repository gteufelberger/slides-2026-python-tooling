import adapter from "@sveltejs/adapter-static";
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

// Check if running in dev mode
const dev = process.argv.includes("dev");

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://svelte.dev/docs/kit/integrations
  // for more information about preprocessors
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter(),
    paths: {
      base: dev ? "" : "/slides-2026-python-tooling", // Repo name subpath for GitHub pages
    },
  },
};

export default config;
