<script setup lang="ts">
import SearchGame from './components/SearchGame.vue'
import GameVideos from './components/GameVideos.vue'
import type { Game, Video } from './types'
import { ref, watch } from 'vue'

const game = ref<Game>()
const videos = ref<Video[]>([])
let interval

const emit = defineEmits<{
  (e: 'videos', value: string): void
}>()

function getVideos(selected_game) {
  clearInterval(interval)
  queryVideos(selected_game)
  setInterval(() => queryVideos(selected_game), 2 * 60000)
}

function queryVideos(selected_game) {
  if (selected_game === undefined) {
    console.warn('Missing ID', selected_game)

    return
  }
  console.log('Getting videos for', selected_game)
  const promise = fetch(`/api/twitch/videos-by-game/${selected_game.twitch_id}`)
  return promise
    .then((response) => {
      return response.json()
    })
    .then((response) => {
      game.value = response.game
      videos.value = response.videos
    })
}
</script>

<template>
  <header>
    <SearchGame @videosSearch="getVideos" />
  </header>

  <main>
    <GameVideos :videos="videos" :game="game" />
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
