<script setup lang="ts">
import SearchGame from './components/SearchGame.vue'
import GameBox from './components/GameBox.vue'
import GameVideos from './components/GameVideos.vue'
import Loading from './components/Loading.vue'
import type { Game, Video } from './types'
import { ref } from 'vue'

const game = ref<Game>()
const isLoading = ref<boolean>(false)
const videos = ref<Video[]>([])
let interval: number | undefined = undefined

const emit = defineEmits<{
  (e: 'videos', value: Game): any
}>()

function getVideos(selected_game: Game) {
  if (interval !== undefined) {
    clearInterval(interval)
  }
  queryVideos(selected_game)
  interval = setInterval(() => queryVideos(selected_game), 2 * 60000)
}

function queryVideos(selected_game: Game) {
  if (selected_game === undefined) {
    return
  }
  game.value = selected_game
  isLoading.value = true

  const promise = fetch(`/api/twitch/videos-by-game/${selected_game.twitch_id}`)
  return promise
    .then((response) => {
      return response.json()
    })
    .then((response) => {
      videos.value = response.videos
      isLoading.value = false
    })
}
</script>

<template>
  <header>
    <SearchGame @videosSearch="getVideos" />
  </header>

  <main>
    <Loading v-if="isLoading" />
    <div v-if="!isLoading">
      <GameBox :game="game" />
      <GameVideos :videos="videos" :game="game" />
    </div>
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
