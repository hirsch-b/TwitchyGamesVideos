<script setup lang="ts">
import { ref, watch } from 'vue'
import type { Game } from './types'

const term = ref('')
const game = ref()
const autocomplete = ref([])

function onChange() {
  getAutocomplete()
}

const emit = defineEmits<{
  (e: 'videosSearch', value: string): void
}>()

function onClick(selected_game) {
  term.value = selected_game.name
  game.value = selected_game
  onSubmit()
}

function onSubmit() {
  // Launch search
  console.log('onSubmit', game)
  if (game.value) {
    console.log('Searching for', game.value)
    emit('videosSearch', game.value)
  }
  autocomplete.value = []
}

function getAutocomplete() {
  const promise = fetch('/api/twitch/games/' + encodeURI(term.value))
  return promise
    .then((response) => {
      return response.json()
    })
    .then((json) => {
      autocomplete.value = json
      if (json.length == 1) {
        game.value = json[0]
        onSubmit()
      } else {
        game.value = undefined
      }
    })
}

function debounce(f, wait) {
  let timeout
  return () => {
    clearTimeout(timeout)
    timeout = setTimeout(() => f(), wait)
  }
}

watch(term, debounce(onChange, 400))
</script>

<template>
  <nav>
    <form v-on:submit="onSubmit()">
      <div>
        <input v-model.trim="term" type="text" placeholder="Search for a game" />
        <ul v-show="autocomplete.length > 0">
          <li v-on:click="() => onClick(game)" v-for="game in autocomplete">{{ game.name }}</li>
        </ul>
      </div>
      <div>
        <button type="button" v-on:click="onSubmit()">Search</button>
      </div>
    </form>
  </nav>
</template>
