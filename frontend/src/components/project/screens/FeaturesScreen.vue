<template>
  <div class="features">
    <DownloadInformationModal
      v-if="isOpenDownloadReportModal"
      :project-id="currentProject.id"
      @close="$emit('close-modal')"
    />

    <div class="features__header">
      <MainLayoutTitleBlock
        :title="currentProject.title"
        :description="currentProject.note"
        :back-page="{
          name: 'workspace',
          routeName: `${currentProject.source}Workspace`,
        }"
        :should-translate="false"
      >
        <TotalResults v-if="numberOfPosts" :total-results="numberOfPosts" />
      </MainLayoutTitleBlock>
      <BaseButton
        :is-not-background="true"
        class="btn-report"
        @click="$emit('download-report')"
      >
        <component
          :is="downloadReportButtonIcon"
          style="--spinner-width: 16px"
        ></component>
        <CustomText text="Download Report" />
      </BaseButton>
    </div>
    <router-view :current-project="currentProject"></router-view>
  </div>
</template>

<script>
import {mapState} from 'vuex'

import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import BaseButton from '@/components/common/BaseButton'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
import TotalResults from '@/components/TotalResults'
import CustomText from '@/components/CustomText'
import DownloadInformationModal from '@/components/project/modals/DownloadInformationModal'
import BaseButtonSpinner from '@/components/BaseButtonSpinner'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'

export default {
  name: 'FeaturesScreen',
  components: {
    MainLayoutTitleBlock,
    BaseButton,
    ReportsUploadIcon,
    TotalResults,
    CustomText,
    DownloadInformationModal,
    BaseButtonSpinner,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
    numberOfPosts: {type: Number, required: true},
    isOpenDownloadReportModal: {type: Boolean, default: false},
  },
  computed: {
    ...mapState({
      downloadingInstantReport: (state) => state.downloadingInstantReport,
    }),
  },
  methods: {
    downloadReportButtonIcon() {
      return this.downloadingInstantReport
        ? 'BaseButtonSpinner'
        : 'ReportsUploadIcon'
    },
  },
}
</script>

<style lang="scss" scoped>
.features {
  display: flex;
  flex-direction: column;
  gap: 30px;

  padding-bottom: 20px;
}
.features__header {
  display: flex;
  justify-content: space-between;

  .btn-report {
    align-self: flex-end;
  }
}
</style>
