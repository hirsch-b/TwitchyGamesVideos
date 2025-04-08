<script setup lang="ts">
import type { Game } from './types'
const props = defineProps<{
  game?: Game
}>()
</script>

<template>
  <div v-if="props.game !== undefined">
    <h1>{{ props.game.name }} (id: {{ props.game.twitch_id }})</h1>
  </div>
</template>

<style>
h1 {
  margin-bottom: 1em;
  margin-top: 1em;
}
</style>
