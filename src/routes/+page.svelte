<script>
  import Reveal from "reveal.js";
  import "reveal.js/dist/reveal.css";
  import "reveal.js/dist/theme/black.css"; // Choose your theme
  import { onMount } from "svelte";
  import TitleContent from "$lib/slides/TitleContent.svelte";
  import GoalContent from "$lib/slides/GoalContent.svelte";

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
      <GoalContent />
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
