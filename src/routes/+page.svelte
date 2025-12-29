<script>
  import Reveal from "reveal.js";
  import "reveal.js/dist/reveal.css";
  import "reveal.js/dist/theme/black.css"; // Choose your theme
  import { onMount } from "svelte";
  import TitleContent from "$lib/slides/TitleContent.svelte";
  import GoalContent from "$lib/slides/GoalContent.svelte";
  import DependencyManagementSection from "$lib/slides/DependencyManagementSection.svelte";
  import FormattingLintingSection from "$lib/slides/FormattingLintingSection.svelte";
  import TypeHintsSection from "$lib/slides/TypeHintsSection.svelte";
  import OtherTipsSection from "$lib/slides/OtherTipsSection.svelte";
  import SummaryContent from "$lib/slides/SummaryContent.svelte";

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
      <DependencyManagementSection />
    </section>
    <section>
      <FormattingLintingSection />
    </section>
    <section>
      <TypeHintsSection />
    </section>
    <section>
      <OtherTipsSection />
    </section>
    <section>
      <SummaryContent />
    </section>
  </div>
</div>

<style>
</style>
