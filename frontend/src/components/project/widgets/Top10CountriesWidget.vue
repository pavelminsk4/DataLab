<template>
  <WidgetsLayout
    v-if="topCountries"
    :title="widgets['top_10_countries_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div class="brands-wrapper">
      <div
        v-for="(item, index) in topCountries"
        :key="'brand' + index"
        class="brand-line"
      >
        <div class="brand-name">
          <span :class="['index', index + 1 > 5 && 'low-index']">{{
            index + 1
          }}</span>
          {{ item.feedlink__country }}
        </div>
        <div class="progress-wrapper">
          <div
            class="progress"
            :style="{width: percentageIndicator(item.country_count)}"
          ></div>
        </div>
        <div class="count">{{ item.country_count }}</div>
      </div>
    </div>
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'Top10CountriesWidget',
  components: {WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_TOP_COUNTRIES_WIDGET](this.projectId)
  },
  computed: {
    ...mapGetters({
      topCountries: get.TOP_COUNTRIES,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    value() {
      return this.topCountries.map((el) => el.country_count)
    },
    labels() {
      return this.topCountries.map((el) => el.feedlink__country)
    },
  },
  methods: {
    ...mapActions([action.GET_TOP_COUNTRIES_WIDGET]),
    percentageIndicator(val) {
      let sum = this.value.reduce(
        (accumulator, currentValue) => accumulator + currentValue
      )

      return ((100 * val) / sum).toFixed().toString() + '%'
    },
  },
}
</script>

<style lang="scss" scoped>
.brands-wrapper {
  display: flex;
  flex-direction: column;

  width: 100%;
  height: 100%;
  margin: 20px 0 0 10px;

  .brand-line {
    display: flex;
    align-items: center;

    margin-bottom: 18px;

    .brand-name {
      min-width: 100px;
      margin-right: 40px;

      white-space: nowrap;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 150%;
    }

    .progress-wrapper {
      width: 100%;
      height: 14px;

      border-radius: 34px;
      background-color: var(--primary-bg-color);

      .progress {
        height: 14px;

        border-radius: 34px;
        background-color: var(--primary-button-color);
      }
    }

    .count {
      width: 50px;
      margin-left: 18px;

      font-style: normal;
      font-weight: 500;
      font-size: 14px;
      line-height: 20px;
    }
  }

  .index {
    margin-right: 18px;

    color: var(--tag-color);
  }

  .low-index {
    margin-right: 18px;

    color: #ffdb5b;
  }
}
</style>
