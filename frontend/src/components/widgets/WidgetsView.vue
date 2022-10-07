<template>
  <grid-layout
    v-model:layout="layout"
    :col-num="4"
    :row-height="30"
    is-draggable
    is-resizable
    vertical-compact
    use-css-transforms
    class="widgets-wrapper"
  >
    <grid-item
      class="widget-item"
      v-for="item in layout"
      :static="item.static"
      :x="item.x"
      :y="item.y"
      :w="item.w"
      :h="item.h"
      :i="item.i"
      :key="item.i"
      :minW="1.3"
      :minH="6"
    >
      <SummaryWidget />
    </grid-item>
  </grid-layout>
</template>

<script>
import VueGridLayout from 'vue3-grid-layout'
import SummaryWidget from '@/components/widgets/SummaryWidget'

export default {
  name: 'WidgetsView',
  components: {
    SummaryWidget,
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
  },
  data() {
    return {
      layout: [{x: 0, y: 0, w: 2, h: 6, i: '0', static: false}],
    }
  },
  methods: {
    itemTitle(item) {
      let result = item.i
      if (item.static) {
        result += ' - Static'
      }
      return result
    },
  },
}
</script>

<style lang="scss" scoped>
.widgets-wrapper {
  margin-top: 30px;

  .widget-item {
    border-radius: 8px;
    border: 1px solid var(--input-border-color);
    background-color: var(--secondary-bg-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);

    color: var(--primary-text-color);
  }
}
</style>

<style>
.vue-grid-layout {
  margin-left: -10px;
}

.vue-grid-item.vue-grid-placeholder {
  border-radius: 8px;
  border: 1px solid var(--input-border-color);
  background-color: var(--secondary-text-color);
}

.vue-resizable-handle {
  background: var(--secondary-text-color);
}
</style>
