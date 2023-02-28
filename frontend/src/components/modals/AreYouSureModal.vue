<template>
  <BaseModal>
    <template #title>
      Are you sure you want to delete {{ itemToDelete.type }}
      <span class="active-option">
        {{ itemToDelete.name }}
      </span>
      ?
    </template>

    <div class="modal-buttons">
      <BaseButton @click.stop="$emit('delete')">Delete</BaseButton>
      <BaseButton :is-not-background="true" @click="$emit('close')">
        Cancel
      </BaseButton>
    </div>
  </BaseModal>
</template>

<script>
import BaseButton from '@/components/common/BaseButton'
import BaseModal from '@/components/modals/BaseModal'

export default {
  name: 'AreYouSureModal',
  components: {BaseModal, BaseButton},
  props: {
    itemToDelete: {
      type: Object,
      default: () => {},
    },
  },
}
</script>

<style lang="scss">
.modal-buttons {
  display: flex;
  gap: 20px;
}

.active-option {
  color: var(--primary-color);
}
</style>
