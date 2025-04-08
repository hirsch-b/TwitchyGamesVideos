<script lang="ts">
import type { Video } from './types'

// defineProps<{
//   videos: Video[]
// }>()
</script>

<template>
  <ul>
    <li v-for="video in videos">{{ video.title }}</li>
  </ul>
</template>

<style scoped></style>
