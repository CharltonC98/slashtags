<template>
  <v-app>
    <v-app-bar
      app
      color="#202020"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="SlashTags Logo"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src= "@/assets/slash_logo.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-text-field
        @keydown.enter="search_videos"
        label="Enter Keyword(s)"
        append-icon="mdi-magnify"
        color="#03dac6"
        v-model="search"
        hide-details
      ></v-text-field>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/CharltonC98/slash-tags"
        target="_blank"
        text
      >
        <span class="mr-2">View on GitHub</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <HelloWorld :msg="videos" />
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import axios from 'axios'

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    search: '',
    videos: []
  }),
  methods: {
    search_videos: function()
    {
      console.log(this.search)
      axios.get('http://127.0.0.1:5000/tags/api/videos',{
        params: {
          query: this.search
        }
      }).then(response => {
        this.videos = response.data
        console.log(this.videos)
      })
    }

  }
};
</script>
