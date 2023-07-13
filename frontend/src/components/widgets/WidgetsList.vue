<template>
  <InteractiveWidgetModal
    v-if="inreractiveDataModal.isShow"
    :widget-id="inreractiveDataModal.widgetId"
    :current-project="currentProject"
    :module-name="moduleName"
    class="interactive-widgets"
    @show-results="updatePageAndCountPosts"
    @close="closeInteractiveModal"
  />

  <component
    :is="`${moduleName}WidgetSettingsModal`"
    v-if="isOpenWidgetSettingsModal"
    :widgetDetails="selectedWidgets[currentWidgetIndex].widgetDetails"
    @close="closeModal"
  />
  <ul class="widgets">
    <li
      v-for="(item, index) in selectedWidgets"
      :key="index"
      :class="['widgets__item', item.isFullWidth && 'grow']"
      :style="{minHeight: item.minHeight, width: listWidth}"
    >
      <component
        :is="`${moduleName}MainWidget`"
        :widgetDetails="item.widgetDetails"
        :isShowDeleteBtn="item.isShowDeleteBtn"
        :isShowSettingsBtn="item.isShowSettingsBtn"
        @open-settings-modal="openModal(item.widgetDetails)"
        @delete-widget="$emit('delete-widget', item.widgetDetails.name)"
      />
    </li>
  </ul>
</template>
<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import OnlineWidgetSettingsModal from '@/components/widgets/online/modals/WidgetSettingsModal'
import SocialWidgetSettingsModal from '@/components/widgets/social/modals/WidgetSettingsModal'
import AccountAnalysisWidgetSettingsModal from '@/components/widgets/account-analysis/modals/WidgetSettingsModal'

import OnlineMainWidget from '@/components/widgets/online/OnlineMainWidget'
import SocialMainWidget from '@/components/widgets/social/SocialMainWidget'
import ComparisonMainWidget from '@/components/widgets/comparison/ComparisonMainWidget'
import AccountAnalysisMainWidget from '@/components/widgets/account-analysis/AccountAnalysisMainWidget'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')
const {mapActions: mapAccounAnalysisAction} =
  createNamespacedHelpers('accountAnalysis')

export default {
  name: 'WidgetsList',
  components: {
    OnlineMainWidget,
    SocialMainWidget,
    ComparisonMainWidget,
    OnlineWidgetSettingsModal,
    SocialWidgetSettingsModal,
    AccountAnalysisWidgetSettingsModal,
    AccountAnalysisMainWidget,
    InteractiveWidgetModal,
  },
  emits: ['delete-widget'],
  props: {
    currentProject: {type: [Array, Object], required: false},
    selectedWidgets: {type: Array, required: true},
    moduleName: {type: String, required: true},
    listWidth: {type: String, default: ''},
  },
  data() {
    return {
      isOpenWidgetSettingsModal: false,
      currentWidget: null,
      currentWidgetIndex: 0,
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
      action.POST_INTERACTIVE_WIDGETS,
    ]),
    ...mapSocialActions({
      postSocialInteractiveData: action.POST_INTERACTIVE_WIDGETS,
    }),
    ...mapAccounAnalysisAction({
      postAccountAnalysisInteractiveData: action.POST_INTERACTIVE_WIDGETS,
    }),
    openModal(widget) {
      this.currentWidgetIndex = this.selectedWidgets.findIndex(
        (element) => element.widgetDetails.name === widget.name
      )
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

    updatePageAndCountPosts(page, countPosts) {
      const interactiveValues = {
        projectId: this.inreractiveDataModal.projectId,
        widgetId: this.inreractiveDataModal.widgetId,
        data: {
          ...this.inreractiveDataModal.data,
          page_number: page,
          posts_per_page: countPosts,
        },
      }

      if (this.moduleName === 'Online') {
        this[action.POST_INTERACTIVE_WIDGETS](interactiveValues)
      }

      if (this.moduleName === 'Social') {
        this.postSocialInteractiveData(interactiveValues)
      }

      if (this.moduleName === 'AccountAnalysis') {
        this.postAccountAnalysisInteractiveData(interactiveValues)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.interactive-widgets {
  z-index: 1001;
}

.widgets {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;

  gap: 30px;
  padding-left: 0px;

  list-style: none;
  .widgets__item {
    width: calc(50% - 15px);
    .summary-widget__container {
      display: block;
    }
  }
  .grow {
    width: 100%;
  }
}
</style>
