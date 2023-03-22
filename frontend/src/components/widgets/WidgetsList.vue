<template>
  <ul class="widgets">
    <li
      v-for="item in selectedWidgets"
      :key="item.i"
      :static="item.static"
      :class="[
        'widgets__item',
        item.name === 'top_10_countries_widget' && 'grow',
      ]"
    >
      <MainWidget :widgetDetails="item.widgetDetails" />
    </li>
  </ul>
</template>
<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import MainWidget from '@/components/widgets/online/MainWidget'

export default {
  name: 'WidgetsList',
  components: {
    MainWidget,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
    selectedWidgets: {type: Array, required: true},
  },
  async created() {
    if (!this.availableWidgets) {
      await this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)
    }
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
  },
}
</script>
<style lang="scss" scoped>
.widgets {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
  list-style: none;
  .widgets__item {
    width: calc(50% - 15px);
    .summary-widget__container {
      display: block;
    }
  }
  .grow {
    display: flex;
    width: 100%;
  }
}
</style>
