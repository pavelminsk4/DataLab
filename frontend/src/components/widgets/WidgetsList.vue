<template>
  <InteractiveWidgetModal
    v-if="inreractiveDataModal.isShow"
    :widget-id="widgetId"
    :current-project="currentProject"
    class="interactive-widgets"
    @close="closeInteractiveModal"
  />

  <component
    :is="`${moduleName}WidgetSettingsModal`"
    v-if="isOpenWidgetSettingsModal"
    :widgetDetails="currentWidget"
    @close="closeModal"
  />
  <ul class="widgets">
    <li
      v-for="(item, index) in selectedWidgets"
      :key="index"
      :class="['widgets__item', item.isFullWidth && 'grow']"
    >
      <component
        :is="`${moduleName}MainWidget`"
        :widgetDetails="item.widgetDetails"
        @open-settings-modal="openModal(item.widgetDetails)"
      />
    </li>
  </ul>
</template>
<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import OnlineWidgetSettingsModal from '@/components/widgets/online/modals/WidgetSettingsModal'
import SocialWidgetSettingsModal from '@/components/widgets/social/modals/WidgetSettingsModal'

import OnlineMainWidget from '@/components/widgets/online/OnlineMainWidget'
import SocialMainWidget from '@/components/widgets/social/SocialMainWidget'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'

export default {
  name: 'WidgetsList',
  components: {
    OnlineMainWidget,
    SocialMainWidget,
    OnlineWidgetSettingsModal,
    SocialWidgetSettingsModal,
    InteractiveWidgetModal,
  },
  emits: [
    'update-page',
    'update-posts-count',
    'set-sorting-value',
    'open-interactive-widget',
    'open-sentiment-interactive-widget',
  ],
  props: {
    currentProject: {type: [Array, Object], required: false},
    selectedWidgets: {type: Array, required: true},
    moduleName: {type: String, required: true},
  },
  data() {
    return {
      isOpenWidgetSettingsModal: false,
      currentWidget: null,
    }
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      inreractiveDataModal: get.INTERACTIVE_DATA_MODAL,
    }),
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.CLEAR_INTERACTIVE_DATA,
    ]),
    updatePage(page, posts) {
      this.$emit('update-page', page, posts)
    },
    updatePosts(page, posts) {
      this.$emit('update-posts-count', page, posts)
    },
    openModal(widget) {
      this.currentWidget = widget
      this.isOpenWidgetSettingsModal = !this.isOpenWidgetSettingsModal
    },
    closeModal() {
      this.togglePageScroll(false)
      this.isOpenWidgetSettingsModal = false
    },

    closeInteractiveModal() {
      this.togglePageScroll(false)
      this[action.CLEAR_INTERACTIVE_DATA]()
    },
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
    min-height: 400px;
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
