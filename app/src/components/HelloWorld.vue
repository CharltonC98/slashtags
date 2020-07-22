<template>
  <v-container>
    <v-expansion-panels 
      v-model="show"
      multiple>
      <v-expansion-panel>
        <v-expansion-panel-header>Tags</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card-text>
            <v-row>
              <h2 class="title mb-2">Description Tags</h2>
              <v-btn icon class="ml-4">
                <v-icon>mdi-content-copy</v-icon>
              </v-btn>
            </v-row>
            <template v-for="video in testarray">
              <v-chip v-for="(tag, idx) in video.descriptionTags" :key="idx" class="ma-2">
                {{ tag }}
              </v-chip>
            </template>
          </v-card-text>
          <v-card-text>
            <v-row>
              <h2 class="title mb-2">Regular Tags</h2>
              <v-btn icon class="ml-4">
                <v-icon>mdi-content-copy</v-icon>
              </v-btn>
            </v-row>
            <template v-for="video in testarray">
              <v-chip v-for="(tag, idx) in video.tags" :key="idx" class="ma-2">
                {{ tag }}
              </v-chip>
            </template>
          </v-card-text>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>Videos</v-expansion-panel-header>
        <v-expansion-panel-content>
          Videos used based on your keyword search
          <v-data-table
            :headers="headers"
            :items="testarray"
            class="elevation-1"
          >
            <template v-slot:item.videoId="{ item }">
              <v-img :src="'https://img.youtube.com/vi/' + item.videoId + '/sddefault.jpg'" style="width: 160px; height: 90px" />
            </template>
          </v-data-table>
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
    props: {
      videos: {
        type: Array
      }
    },
    data: () => ({
      headers: [
        {
          text: 'Video',
          align: 'start',
          sortable: false,
          value: 'videoId',
        },
        { text: 'Title', value: 'title', sortable: false},
        { text: 'View Count', value: 'viewCount'},
        { text: 'Like Count', value: 'likeCount' },
        { text: 'Dislike Count', value: 'dislikeCount' },
      ],
      testarray: [
        {
          "videoId":"sqYQkACbsfc",
          "title":"Responding to Wilbur's comments.",
          "description":"yeyeyeyeyeyeyeyeyeye",
          "descriptionTags": ["ludwig", "stream", "clips"],
          "tags":["ludwig","ludwigahgren","ahgren","gaming","chat","stream","decides","lud"],
          "viewCount":"282614",
          "likeCount":
          "15524",
          "dislikeCount":"122"
        },
      ],
      show: []
    }),
    watch: {
    videos: function() {
      console.log(this.videos);
      this.show = [0,1]
      }
    }
  }
</script>
