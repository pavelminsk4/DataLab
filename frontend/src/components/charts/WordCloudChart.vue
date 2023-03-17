<template>
  <vue-word-cloud
    :words="words"
    :font-size-ratio="3"
    :spacing="1"
    font-family="Poppins"
    class="word-cloud-wrapper"
  >
    <template v-slot="{text, weight}">
      <div :title="weight" class="keyword">
        <div class="tooltip-wrapper">
          <BaseTooltip arrow-position="bottom" class="tooltip">
            <div class="title">{{ capitalizeFirstLetter(text) }}</div>
            <div class="title">Results: {{ getCount(text) }} %</div>
          </BaseTooltip>
        </div>

        <div class="word">{{ capitalizeFirstLetter(text) }}</div>
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
      return this.chartValues[0].data[labelIndex].toFixed(2)
    },
  },
}
</script>

<style lang="scss" scoped>
.keyword {
  position: relative;

  .tooltip-wrapper {
    position: absolute;
    top: -50px;
    right: 0;

    display: none;

    z-index: 10000 !important;

    .tooltip {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;

      font-size: 14px;

      z-index: 100000 !important;

      .title {
        color: var(--typography-primary-color);
      }
    }
  }

  .word {
    z-index: -1;
  }

  &:hover {
    .tooltip-wrapper {
      display: flex;
      z-index: 100000 !important;
    }
  }
}
</style>
