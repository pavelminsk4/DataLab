<template>
  <BaseModal modal-frame-style="width:90vw;" class="working-modal">
    <TFSWorkingScreen :post="postInfo" />
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import TFSWorkingScreen from '@/components/twenty-four-seven/modals/screens/TFSWorkingScreen'

export default {
  name: 'TFSWorkingModal',
  components: {BaseModal, TFSWorkingScreen},
  props: {
    postInfo: {type: Object, required: true},
  },
}
</script>

<style lang="scss">
.working-modal {
  .base-modal-body > .title {
    height: 50px;
  }
}
</style>
