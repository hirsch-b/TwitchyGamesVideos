<script setup lang="ts">
import { ref, watch } from 'vue'
import type { Game } from '../types'

const isLoading = ref<boolean>(false)
const isAutocompleteOpen = ref<boolean>(false)
const term = ref<string>('')
const game = ref<Game>()
const autocomplete = ref<Game[]>([])

function onChange() {
  getAutocomplete()
}

const emit = defineEmits<{
  (e: 'videosSearch', value: Game): void
}>()

function onClick(selected_game: Game) {
  term.value = selected_game.name
  game.value = selected_game
  onSubmit()
}

function onSubmit() {
  if (game.value) {
    emit('videosSearch', game.value)
  }
  autocomplete.value = []
  isAutocompleteOpen.value = false
}

function getAutocomplete() {
  const promise = fetch('/api/twitch/games/' + encodeURI(term.value))
  isLoading.value = true
  isAutocompleteOpen.value = true
  autocomplete.value = []
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
        isLoading.value = false
      }
    })
}

function debounce(f: () => void, wait: number) {
  let timeout: number
  return () => {
    clearTimeout(timeout)
    timeout = setTimeout(() => f(), wait)
  }
}

function closeAutocomplete() {
  autocomplete.value = []
  isAutocompleteOpen.value = false
}

watch(term, debounce(onChange, 400))
</script>

<template>
  <nav>
    <form v-on:submit="onSubmit()">
      <div>
        <input v-model.trim="term" type="text" placeholder="Search for a game" />
        <div v-if="isAutocompleteOpen" class="autocomplete">
          <button type="button" v-on:click="closeAutocomplete">X</button>
          <ul>
            <li v-if="isLoading">Loading</li>
            <li v-on:click="() => onClick(game)" v-for="game in autocomplete">{{ game.name }}</li>
          </ul>
        </div>
      </div>
      <div>
        <button type="button" v-on:click="onSubmit()">Search</button>
      </div>
    </form>
  </nav>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: row;
}
div.autocomplete {
  z-index: 1337;
  position: absolute;
  padding: 5px;
  background: #5f5f5f;
  max-height: 400px;
  overflow-y: scroll;
}
ul {
  padding: 0px;
  list-style: none;
}
li {
  padding: 0px 5px;
}
li:hover {
  background: #0e0e0ea9;
  /* padding: 5px; */
}
</style>
