<script>
  import Reveal from "reveal.js";
  import Markdown from "reveal.js/plugin/markdown/markdown.esm.js";
  import "reveal.js/dist/reveal.css";
  import "reveal.js/dist/theme/black.css"; // Choose your theme
  import { onMount } from "svelte";
  import TitleSection from "$lib/sections/TitleSection.svelte";
  import GoalSection from "$lib/sections/GoalSection.svelte";
  import DependencyManagementSection from "$lib/sections/DependencyManagementSection.svelte";
  import FormattingLintingSection from "$lib/sections/FormattingLintingSection.svelte";
  import TypeHintsSection from "$lib/sections/TypeHintsSection.svelte";
  import SummarySection from "$lib/sections/SummarySection.svelte";
  import SidenoteAstralSection from "$lib/sections/SidenoteAstralSection.svelte";
  import FeedbackSection from "$lib/sections/FeedbackSection.svelte";

  onMount(() => {
    Reveal.initialize({
      slideNumber: true,
      plugins: [Markdown],
    });
  });
</script>

<div class="reveal">
  <div class="slides">
    <TitleSection />
    <GoalSection />
    <DependencyManagementSection />
    <FormattingLintingSection />
    <TypeHintsSection />
    <SidenoteAstralSection />
    <SummarySection />
    <FeedbackSection />
  </div>
</div>

<style>
</style>
