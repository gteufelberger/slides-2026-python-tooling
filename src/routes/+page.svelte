<script>
  import Reveal from "reveal.js";
  import "reveal.js/dist/reveal.css";
  import "reveal.js/dist/theme/black.css"; // Choose your theme
  import { onMount } from "svelte";
  import TitleSection from "$lib/slides/TitleSection.svelte";
  import GoalSection from "$lib/slides/GoalSection.svelte";
  import DependencyManagementSection from "$lib/slides/DependencyManagementSection.svelte";
  import FormattingLintingSection from "$lib/slides/FormattingLintingSection.svelte";
  import TypeHintsSection from "$lib/slides/TypeHintsSection.svelte";
  import OtherTipsSection from "$lib/slides/OtherTipsSection.svelte";
  import SummarySection from "$lib/slides/SummarySection.svelte";
  import SidenoteAstralSection from "$lib/slides/SidenoteAstralSection.svelte";

  onMount(() => {
    Reveal.initialize({
      slideNumber: true,
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
    <OtherTipsSection />
    <SummarySection />
  </div>
</div>

<style>
</style>
