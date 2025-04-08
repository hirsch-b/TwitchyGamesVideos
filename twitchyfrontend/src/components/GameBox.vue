<script setup lang="ts">
import type { Game } from './types'
const props = defineProps<{
  game?: Game
}>()
</script>

<template>
  <div v-if="props.game !== undefined">
    <h1>{{ props.game.name }}</h1>
  </div>
</template>
