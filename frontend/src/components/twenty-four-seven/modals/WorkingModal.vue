<template>
  <BaseModal modal-frame-style="width:90vw;" class="working-modal">
    <WorkingScreen :post="postInfo"
  /></BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal.vue'
import WorkingScreen from '@/components/twenty-four-seven/modals/screens/WorkingScreen'

export default {
  name: 'WorkingModal',
  components: {BaseModal, WorkingScreen},
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
