<template>
  <BaseModal>
    <div class="question">
      <slot>
        Are you sure you want to delete {{ itemToDelete.type }}
        <span>
          {{ itemToDelete.name }}
        </span>
        ?
      </slot>
    </div>

    <div class="modal-buttons">
      <BaseButton @click.stop="$emit('delete')">Delete</BaseButton>
      <BaseButton :is-not-background="true" @click="$emit('close')">
        Cancel
      </BaseButton>
    </div>
  </BaseModal>
</template>

<script>
import BaseButton from '@/components/buttons/BaseButton'
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

.question {
  margin-bottom: 35px;

  span {
    color: var(--primary-button-color);
  }
}
</style>
