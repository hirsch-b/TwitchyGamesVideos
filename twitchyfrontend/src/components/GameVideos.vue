<script setup lang="ts">
import GameBox from './GameBox.vue'
import type { Game, Video } from './types'

const props = defineProps<{
  videos?: Video[]
  game?: Game
}>()

function thumb(vid: string, width: number, height: number) {
  if (vid.startsWith('https://vod-secure.twitch.tv/_404/')) {
    return `//picsum.photos/${width}/${height}`
  }
  return vid.replace('%{width}', width).replace('%{height}', height)
}
</script>

<template>
  <GameBox :game="props.game" />
  <ul v-show="props.videos !== undefined">
    <li
      v-for="video in props.videos"
      :style="{ backgroundImage: `${thumb(video.thumbnail_url, 640, 480)}` }"
    >
      <a :href="video.url">
        <h2>{{ video.title || 'No title' }}</h2>
      </a>
    </li>
  </ul>
</template>

<style scoped>
ul {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

li {
  width: 320px;
  height: 180px;
  position: relative;
  display: block;
  background-size: cover;
}
h2 {
  font-size: 1.2em;
  position: absolute;
  top: 0px;
  left: 2.5px;
  padding: 5px;
  overflow: hidden;
  background: #3d3d3d93;
  width: 100%;
  height: 100%;
}
</style>
