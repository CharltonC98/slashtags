<template>
  <v-container>
    <v-expansion-panels>
      <v-expansion-panel>
        <v-expansion-panel-header>Tags</v-expansion-panel-header>
        <v-expansion-panel-content>
          <!-- DESC AND REG TAGS SEPERATED -->
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>Videos</v-expansion-panel-header>
        <v-expansion-panel-content>
          Videos used based on your keyword search
          <v-data-table
            :headers="headers"
            :items="videos"
            class="elevation-1"
          ></v-data-table>
            <!-- <template v-slot:item.thumbnail="{ item }">
                <img :src="'https://img.youtube.com/vi/' + item.id + '/sddefault.jpg' + item.thumbnail" style="width: 160px; height: 120px" />
            </template> -->
        </v-expansion-panel-content>
      </v-expansion-panel>
  </v-expansion-panels>

    <v-row class="text-center">
      <v-col class="mb-4">
        <h5 class=" headline font-weight-bold mb-3">
          About
        </h5>

        <p class="subheading font-weight-regular">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
          et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
          aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
          officia deserunt mollit anim id est laborum.
        </p>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
      headers: [
        {
          text: 'Video',
          align: 'start',
          sortable: false,
          value: 'thumbnail',
        },
        { text: 'Title', value: 'title', sortable: false},
        { text: 'View Count', value: 'viewCount'},
        { text: 'Like Count', value: 'likeCount' },
        { text: 'Dislike Count', value: 'dislikeCount' },
      ]
    }),
    videos: []
  }
</script>
