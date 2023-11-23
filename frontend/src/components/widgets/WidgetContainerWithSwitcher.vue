<template>
  <div class="container">
    <slot></slot>

    <WidgetsSwitcher
      v-if="tabs.length"
      v-model="activeTab"
      :tabs="tabs"
      :isSentiment="true"
    />
  </div>
</template>

<script>
import WidgetsSwitcher from '@components/layout/WidgetsSwitcher'

export default {
  name: 'WidgetContainerWithSwitcher',
  components: {WidgetsSwitcher},
  props: {
    tabs: {type: Array, required: true},
    widgetMaxHeight: {type: String, default: '450px'},
  },
  data() {
    return {
      newActiveTab: '',
    }
  },
  computed: {
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
        this.$emit('switch-tab', newTab)
      },
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  flex-direction: column;
  align-items: center;

  width: 100%;
  max-height: v-bind(widgetMaxHeight);
  height: 100%;
}
</style>
