<script setup lang="ts">
import SearchGame from './components/SearchGame.vue'
import GameVideos from './components/GameVideos.vue'
import { ref } from 'vue'
const videos = ref([])
</script>

<template>
  <header>
    <SearchGame />
  </header>

  <main>
    <GameVideos />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}
</style>
