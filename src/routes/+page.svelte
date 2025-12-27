<script>
  import Reveal from "reveal.js";
  import "reveal.js/dist/reveal.css";
  import "reveal.js/dist/theme/black.css"; // Choose your theme
  import { onMount } from "svelte";

  onMount(() => {
    Reveal.initialize({});
  });
</script>

<div class="reveal">
  <div class="slides">
    <section>
      <h1>Hello, World!</h1>
      <p>First slide</p>
    </section>

    <section>
      <h2>Second Slide</h2>
      <ul>
        <li>Point 1</li>
        <li>Point 2</li>
      </ul>
    </section>
  </div>
</div>

<style>
</style>
