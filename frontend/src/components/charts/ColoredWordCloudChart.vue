<template>
  <div class="word-cloud-chart-wrapper">
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
              <span class="title">Results: {{ getCount(text, item) }} %</span>
            </BaseTooltip>
          </div>

          <div class="word" @click="openInteractiveWidget(text, item)">
            {{ capitalizeFirstLetter(text) }}
          </div>
        </div>
      </template>
    </vue-word-cloud>

    <div v-if="chartValues[0].hasLegends" class="legends">
      <div v-for="item in chartValues" :key="item.type" class="legends__item">
        <div :style="`--mark-color: ${item.color};`" class="legends__mark" />
        <span class="legends__label">{{ item.type }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import VueWordCloud from 'vuewordcloud'
import {capitalizeFirstLetter} from '@/lib/utilities'

import BaseTooltip from '@/components/BaseTooltip'

export default {
  name: 'ColoredWordCloudChart',
  components: {BaseTooltip, VueWordCloud},
  emits: ['open-interactive-data'],
  props: {
    labels: {type: Array, default: () => []},
    hasAnimation: {type: Boolean, default: true},
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
      const MAX_WEIGHT = 60
      const MIN_WIGHT = 14
      const deltaWeight = MAX_WEIGHT - MIN_WIGHT

      return sentimentData.labels.map((label, index) => {
        const currentWeight =
          (sentimentData.data[index] / 100) * deltaWeight + MIN_WIGHT
        return {
          text: label,
          weight: currentWeight,
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
.word-cloud-chart-wrapper {
  position: relative;

  display: flex;
  justify-content: center;

  width: 100%;
  height: 100%;
}

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

.legends {
  position: absolute;
  top: calc(100% + 10px);

  display: flex;
  justify-content: center;

  gap: 12px;

  &__item {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  &__mark {
    width: 20px;
    height: 10px;
    background-color: var(--mark-color);
  }

  &__label {
    font-size: 12px;
    color: var(--typography-secondary-color);
  }
}
</style>

<style lang="scss">
.word-cloud-wrapper {
  transition > div {
    &:hover {
      z-index: 3;
    }
  }

  &:hover {
    z-index: 3;
  }
}
</style>
