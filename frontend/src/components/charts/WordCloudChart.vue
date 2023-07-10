<template>
  <vue-word-cloud
    :words="words"
    :font-size-ratio="3"
    :spacing="1"
    :animation-duration="hasAnimation ? 1000 : 0"
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

        <div class="word" @click="openInteractiveWidget(text)">
          {{ capitalizeFirstLetter(text) }}
        </div>
      </div>
    </template>
  </vue-word-cloud>
</template>

<script>
import {capitalizeFirstLetter} from '@/lib/utilities'

import VueWordCloud from 'vuewordcloud'
import BaseTooltip from '@/components/BaseTooltip'

export default {
  name: 'WordCloudChart',
  components: {BaseTooltip, VueWordCloud},
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Array, default: () => []},
    hasAnimation: {type: Boolean, default: true},
  },
  computed: {
    words() {
      const length = this.chartValues[0].data.length

      return this.chartValues[0].data.map((data, index) => {
        return {
          text: this.labels[index],
          weight: ((length - index) * 60) / length,
          fontWeight: 500,
          color: `rgba(42, 0, 255, ${(length - index) / length})`,
        }
      })
    },
  },
  methods: {
    capitalizeFirstLetter,
    getCount(word) {
      const labelIndex = this.labels.indexOf(word)
      return this.chartValues[0].data[labelIndex]?.toFixed(2)
    },
    openInteractiveWidget(word) {
      this.$emit('open-interactive-data', word, this.chartValues[0]?.tab)
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
