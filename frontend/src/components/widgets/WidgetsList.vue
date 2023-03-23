<template>
  <WidgetSettingsModal
    v-if="isOpenWidgetSettingsModal"
    :widgetDetails="currentWidget"
    @close="closeModal"
    @open-interactive-widget="openInteractiveData"
    @open-sentiment-interactive="openSentimentInteractiveData"
  />
  <ul class="widgets">
    <li
      v-for="item in selectedWidgets"
      :key="item.i"
      :static="item.static"
      :class="['widgets__item', item.isFullWidth && 'grow']"
    >
      <MainWidget
        :widgetDetails="item.widgetDetails"
        @open-settings-modal="openModal(item.widgetDetails)"
        @open-interactive-data="openInteractiveData"
        @open-sentiment-interactive="openSentimentInteractiveData"
      />
    </li>
  </ul>
</template>
<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import WidgetSettingsModal from '@/components/widgets/online/modals/WidgetSettingsModal'

import MainWidget from '@/components/widgets/online/MainWidget'

export default {
  name: 'WidgetsList',
  components: {
    MainWidget,
    WidgetSettingsModal,
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
    }),
  },
  methods: {
    ...mapActions([action.UPDATE_AVAILABLE_WIDGETS]),
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
    openInteractiveData(val, widgetId, fieldName) {
      this.$emit('open-interactive-widget', val, widgetId, fieldName)
    },
    openSentimentInteractiveData(source, sentiment, widgetId) {
      this.$emit(
        'open-sentiment-interactive-widget',
        source,
        sentiment,
        widgetId
      )
    },
    closeModal() {
      this.togglePageScroll(false)
      this.isOpenWidgetSettingsModal = false
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
