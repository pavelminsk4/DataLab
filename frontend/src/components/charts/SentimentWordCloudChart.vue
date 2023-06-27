<template>
  <vue-word-cloud
    v-for="(item, index) in chartValues"
    :key="'sentiment-keywords-' + index"
    :words="words(item)"
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
            <span class="title">Results: {{ getCount(text, item) }} %</span>
          </BaseTooltip>
        </div>

        <div class="word" @click="openInteractiveWidget(text, item)">
          {{ capitalizeFirstLetter(text) }}
        </div>
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
  emits: ['open-interactive-data'],
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Array, default: () => []},
    isLegendDisplayed: {type: Boolean, default: true, required: false},
  },
  methods: {
    capitalizeFirstLetter,
    getCount(word, sentimentData) {
      const index = sentimentData.labels.indexOf(word)
      return sentimentData.data[index]?.toFixed(2)
    },
    words(sentimentData) {
      return sentimentData.labels.map((label) => {
        return {
          text: label,
          weight: 18,
          fontWeight: 500,
          color: sentimentData.color,
        }
      })
    },
    openInteractiveWidget(word, item) {
      this.$emit('open-interactive-data', word, item.type)
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

  &:hover {
    z-index: 200;
  }
}
</style>
