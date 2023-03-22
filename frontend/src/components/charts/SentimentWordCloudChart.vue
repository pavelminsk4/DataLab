<template>
  <vue-word-cloud
    :words="words"
    :font-size-ratio="3"
    :spacing="1"
    font-family="Poppins"
    class="word-cloud-wrapper"
  >
    <template v-slot="{text}">
      <div class="keyword">
        <div class="tooltip-wrapper">
          <BaseTooltip arrow-position="bottom" class="tooltip">
            <div class="title">{{ capitalizeFirstLetter(text) }}</div>
            <span class="title">Results: {{ getCount(text) }} %</span>
          </BaseTooltip>
        </div>

        <div class="word">{{ capitalizeFirstLetter(text) }}</div>
      </div>
    </template>
  </vue-word-cloud>
</template>

<script>
import VueWordCloud from 'vuewordcloud'
import {capitalizeFirstLetter} from '@/lib/utilities'

import BaseTooltip from '@/components/BaseTooltip'

export default {
  name: 'SentimentWordCloudChart',
  components: {BaseTooltip, VueWordCloud},
  props: {
    chartValues: {type: Array, default: () => []},
    chartLabels: {type: Array, default: () => []},
  },
  computed: {
    words() {
      return [
        {
          text: this.chartLabels[0],
          weight: 40,
          fontWeight: 500,
          color: this.chartValues[0].color,
        },
      ]
    },
  },
  mounted() {
    console.log(this.words)
  },
  methods: {
    capitalizeFirstLetter,
    getCount(word) {
      return word
    },
  },
}
</script>

<style lang="scss" scoped>
.keyword {
  position: relative;

  cursor: pointer;

  .tooltip-wrapper {
    position: absolute;
    right: -96px;
    top: -66px;
    transform: translate(-50%, -50%);

    display: none;

    .tooltip {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;

      .title {
        font-size: 14px;
        color: var(--typography-primary-color);
      }
    }
  }

  &:hover {
    .tooltip-wrapper {
      display: flex;
    }
  }
}
</style>

<style lang="scss">
.word-cloud-wrapper {
  transition > div {
    &:hover {
      z-index: 200;
    }
  }
}
</style>
