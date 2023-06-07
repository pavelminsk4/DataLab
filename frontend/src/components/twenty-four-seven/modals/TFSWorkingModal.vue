<template>
  <BaseModal modal-frame-style="width:90vw;" class="working-modal">
    <div class="working-wrapper">
      <ContentWithPosts :post="post" :related-content="relatedContent" />

      <section class="working-content-wrapper">
        <div class="panel-tabs">
          <span
            v-for="(item, index) in panelTabs"
            :key="item + index"
            :class="['tab', item === activeTab && 'active-tab']"
            @click="changeTab(item)"
          >
            {{ item }}
          </span>
        </div>

        <div class="content-wrapper">
          <TFSSummaryTab
            v-if="activeTab === 'Summary' || activeTab === 'Q&A Check'"
            :post="post"
            @save-summary="saveSummary"
          />

          <component
            v-else
            :is="`TFS${stringToPascalCase(activeTab)}Tab`"
            :post="post"
            @save-summary="saveSummary"
          />
        </div>
      </section>
    </div>
  </BaseModal>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {stringToPascalCase} from '@/lib/utilities'
import {modalTabs} from '@/lib/configs/tfsStatusesConfig'

import BaseModal from '@/components/modals/BaseModal'
import TFSOriginalContentTab from '@/components/twenty-four-seven/TFSOriginalContentTab'
import TFSStoryReportTab from '@/components/twenty-four-seven/TFSStoryReportTab'
import TFSSummaryTab from '@/components/twenty-four-seven/TFSSummaryTab'
import ContentWithPosts from '@/components/twenty-four-seven/ContentWithPosts'

const {mapState, mapActions} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSWorkingModal',
  components: {
    BaseModal,
    TFSSummaryTab,
    TFSOriginalContentTab,
    TFSStoryReportTab,
    ContentWithPosts,
  },
  props: {
    post: {type: Object, required: true},
  },
  computed: {
    ...mapState(['items', 'relatedContent']),
    activeTab() {
      return this.$route.query.tab
    },
    panelTabs() {
      return modalTabs[this.post.status]
    },
  },
  created() {
    this[action.GET_TFS_RELATED_CONTENT](this.post.id)
  },
  methods: {
    ...mapActions([
      action.GET_TFS_RELATED_CONTENT,
      action.UPDATE_TFS_ITEM_DATA,
    ]),
    stringToPascalCase,
    changeTab(tabName) {
      this.$router.push({
        name: 'TFSDashboard',
        query: {modal: 'Working', tab: tabName},
      })
    },
    async saveSummary(header, text) {
      await this[action.UPDATE_TFS_ITEM_DATA]({
        projectId: this.post.project,
        itemId: this.post.id,
        value: {header, text, status: this.post.status},
        page: 1,
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.working-wrapper {
  display: flex;

  width: 100%;

  .working-content-wrapper {
    flex: 1;
    padding: 24px;
    margin: -24px -24px -24px 24px;

    background-color: var(--background-primary-color);
    .panel-tabs {
      display: flex;
      flex-wrap: nowrap;
      justify-content: space-between;
      gap: 10px;

      .tab {
        position: relative;

        width: 100%;
        padding: 4px 18px;

        background: var(--background-additional-color);
        border-radius: 10px;

        cursor: pointer;

        text-align: center;
        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
      }

      .active-tab {
        color: var(--button-text-color);
        background-color: var(--button-primary-color);
      }
    }

    .content-wrapper {
      display: flex;
      flex-direction: column;

      margin-top: 22px;
    }
  }
}
</style>

<style lang="scss">
.working-modal {
  .base-modal-body > .title {
    height: 50px;
  }
}
</style>
