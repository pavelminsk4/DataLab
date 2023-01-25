<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ clippingFeedContent.title }}</div>

    <BasicSettingsScreen
      v-if="panelName === 'General'"
      :is-aggregation-period="false"
      :period="clippingFeedContent.aggregation_period"
      :widget-title="clippingFeedContent.title"
      :widget-description="clippingFeedContent.description"
      class="settings-wrapper"
      @save-changes="saveOptions"
    />
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import BasicSettingsScreen from '@/components/project/widgets/modals/screens/BasicSettingsScreen'

export default {
  name: 'ClippingFeedContentWidgetModal',
  components: {BasicSettingsScreen, BaseModal},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      title: '',
      description: '',
      panelName: 'General',
    }
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS}),
    clippingFeedContent() {
      return this.widgets['clipping_feed_content_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          clipping_feed_content_widget: {
            id: this.clippingFeedContent.id,
            title: this.title || this.clippingFeedContent.title,
            description:
              this.description || this.clippingFeedContent.description,
          },
        },
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
  },
}
</script>

<style lang="scss" scoped>
.main-title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}
</style>
