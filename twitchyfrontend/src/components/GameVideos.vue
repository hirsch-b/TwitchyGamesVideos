<script setup lang="ts">
import type { Game, Video } from '../types'

const props = defineProps<{
  videos?: Video[]
  game?: Game
}>()

function thumb(vid: string, width: string, height: string) {
  return `url(${vid.replace('%{width}', width).replace('%{height}', height)})`
}
</script>

<template>
  <ul v-show="props.videos !== undefined">
    <li
      v-for="video in props.videos"
      :style="{ backgroundImage: thumb(video.thumbnail_url, '320', '180') }"
    >
      <a :href="video.url">
        <h2>{{ video.user_name }} - {{ video.title || 'No title' }}</h2>
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
  justify-content: center;
  gap: 15px;
}

li {
  position: relative;
  width: 320px;
  height: 180px;
  display: block;
  background-size: cover;
}

h2 {
  font-size: 1.2em;
  position: absolute;
  top: 0px;
  padding: 5px;
  overflow: hidden;
  background: #3d3d3d93;
  width: 100%;
  height: 100%;
}
</style>
