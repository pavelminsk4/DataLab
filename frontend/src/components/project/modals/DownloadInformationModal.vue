<template>
  <BaseModal
    modal-frame-style="width: auto; height: auto;"
    title="Downloading Report"
  >
    <section class="downloading-reports">
      <div class="downloading-reports__message-container">
        <p>Your report is being created please wait.</p>
        <BaseButtonSpinner
          style="--spinner-width: 16px"
          class="downloading-reports__spinner"
        />
      </div>

      <BaseButton class="downloading-reports__close-btn" @click="$emit('close')"
        >Close</BaseButton
      >
    </section>
  </BaseModal>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'

import BaseButton from '@/components/common/BaseButton'
import BaseButtonSpinner from '@/components/BaseButtonSpinner'
import BaseModal from '@/components/modals/BaseModal'

const {mapState} = createNamespacedHelpers('social')

export default {
  name: 'DownloadReportModal',
  components: {
    BaseButton,
    BaseButtonSpinner,
    BaseModal,
  },
  props: {
    projectId: {type: [Number, String], required: true},
  },
  computed: {
    ...mapState(['downloadingInstantReport']),
  },
}
</script>

<style lang="scss" scoped>
.downloading-reports {
  display: flex;
  flex-direction: column;

  &__message-container {
    display: flex;
    align-items: center;
    gap: 5px;

    font-size: 16px;
  }

  &__close-btn {
    align-self: flex-end;

    margin-top: 20px;
  }
}
</style>
