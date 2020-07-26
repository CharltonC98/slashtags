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
              <v-btn icon class="ml-4" v-on:click="copy_desc">
                <v-icon>mdi-content-copy</v-icon>
              </v-btn>
            </v-row>
            <v-chip-group 
            multiple 
            max="3"
            active-class="teal lighten-3--text"
            v-model="descGroup">
              <v-chip v-for="(tag, i) in Object.keys(descTags)" :key="`A-${i}`" class="ma-2">
                {{ tag }}
              </v-chip>
            </v-chip-group>
          </v-card-text>

          <v-card-text>
            <v-row>
              <h2 class="title mb-2">Regular Tags</h2>
              <v-btn icon class="ml-4" v-on:click="copy_reg">
                <v-icon>mdi-content-copy</v-icon>
              </v-btn>
            </v-row>
              <v-chip v-for="(tag, i) in Object.keys(regTags)" :key="`B-${i}`" :color="regScale[i]" class="ma-2">
                {{ tag }}
              </v-chip>
          </v-card-text>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Videos</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-data-table
            :headers="headers"
            :items="videos"
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
          SlashTags is a tool for recomending tags based on keyword(s) and viewing related video statistics <br>
          Look at the README to get started <br> <br>
          Created by Cameron Charlton - <a href="https://twitter.com/huhmit"> Twitter </a> - <a href="youtube.com/c/Hermit_CS"> YouTube </a>
        </p>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import chroma from 'chroma-js'
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
      testarray: {
        "videoId":"sqYQkACbsfc",
        "title":"Responding to Wilbur's comments.",
        "description":"yeyeyeyeyeyeyeyeyeye",
        "descriptionTags": ["ludwig", "stream", "clips", "1", "2", "3"],
        "tags":["ludwig","ludwigahgren","ahgren","gaming","chat","stream","decides","lud"],
        "viewCount":"282614",
        "likeCount":
        "15524",
        "dislikeCount":"122",
      },
      descTags: {},
      regTags: {},
      descScale: {},
      regScale: {},
      descGroup: [],
      show: []
    }),
    methods: {
      copy_desc: function() {
        var copy = ""
        for (var i = 0; i < Object.keys(this.descTags).length; i++) { 
          if (this.descGroup.includes(i)) {
            copy += "#" + Object.keys(this.descTags)[i] + " "
          }
        }
        var dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
        dummy.value = copy;
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
      },
      copy_reg: function() {
        var dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
        dummy.value = Object.keys(this.regTags).toString();
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
      }
    },
    watch: {
    videos: function() {
      console.log(this.videos);
      this.show = [0,1]
      
      this.videos.forEach(element => {
        element.tags.forEach(tag => {
          if (!(tag.toLowerCase() in this.regTags)) {
            this.regTags[tag] = 1
          }
          else {
            this.regTags[tag.toLowerCase()] += 1
          }
        })
        element.descriptionTags.forEach(tag => {
          if (!(tag.toLowerCase() in this.descTags)) {
            this.descTags[tag] = 1
          }
          else {
            this.descTags[tag.toLowerCase()] += 1
          }
        })
      });

      this.regScale = chroma
      .scale(["#26A69A", "#80CBC4"])
      .mode("rgb")
      .colors(Object.keys(this.regTags).length);
      
      this.descScale = chroma
      .scale(["#26A69A", "#80CBC4"])
      .mode("rgb")
      .colors(Object.keys(this.descTags).length);
      }
    }
  }
</script>
