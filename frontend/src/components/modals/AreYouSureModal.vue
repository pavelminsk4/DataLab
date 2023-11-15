<template>
  <BaseModal>
    <template #title>
      <CustomText
        tag="span"
        :text="`Are you sure you want to delete ${itemToDelete.type}`"
      />
      <span class="active-option"> &nbsp; {{ itemToDelete.name }} </span>
      ?
    </template>

    <div class="modal-buttons">
      <BaseButton @click.stop="$emit('delete')">
        <CustomText text="Delete" />
      </BaseButton>
      <BaseButton :is-not-background="true" @click="$emit('close')">
        <CustomText text="Cancel" />
      </BaseButton>
    </div>
  </BaseModal>
</template>

<script>
import CustomText from '@components/CustomText'
import BaseButton from '@components/common/BaseButton'
import BaseModal from '@components/modals/BaseModal'

export default {
  name: 'AreYouSureModal',
  components: {BaseModal, BaseButton, CustomText},
  props: {
    itemToDelete: {type: Object, default: () => {}},
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
