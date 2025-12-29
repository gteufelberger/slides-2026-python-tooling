<script>
  import Reveal from "reveal.js";
  import "reveal.js/dist/reveal.css";
  import "reveal.js/dist/theme/black.css"; // Choose your theme
  import { onMount } from "svelte";
  import TitleContent from "$lib/slides/TitleContent.svelte";

  onMount(() => {
    Reveal.initialize({
      slideNumber: true,
    });
  });
</script>

<div class="reveal">
  <div class="slides">
    <section>
      <TitleContent />
    </section>

    <section>
      <h2>Goal</h2>
      <p>
        Show you what tools are out there so that you can decide what to use to
        be more productive
      </p>
    </section>
    <section>
      Dependency management
      <section>TODO</section>
    </section>
    <section>
      Formatting & Linting
      <section>TODO</section>
    </section>
    <section>
      Type hints
      <section>TODO</section>
    </section>
    <section>
      Other development tips
      <section>TODO</section>
    </section>
    <section>Summary</section>
  </div>
</div>

<style>
</style>
