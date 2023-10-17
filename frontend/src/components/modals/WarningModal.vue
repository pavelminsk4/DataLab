<template>
  <BaseModal>
    <template #title>
      <CustomText tag="div">
        Are you sure about the words you entered?
      </CustomText>
    </template>

    <CustomText tag="div" class="text">
      After clicking the 'Approve' button, you will not be able to edit the
      project keywords. <br />
      Please make sure that the keywords entered are correct.
    </CustomText>

    <div class="modal-buttons">
      <BaseButton @click.stop="$emit('approve')">
        <CustomText text="Approve" />
      </BaseButton>
      <BaseButton :is-not-background="true" @click="$emit('close')">
        <CustomText text="Cancel" />
      </BaseButton>
    </div>
  </BaseModal>
</template>

<script>
import CustomText from '@/components/CustomText'
import BaseButton from '@/components/common/BaseButton'
import BaseModal from '@/components/modals/BaseModal'

export default {
  name: 'WarningModal',
  components: {BaseModal, BaseButton, CustomText},
}
</script>

<style lang="scss">
.modal-buttons {
  display: flex;
  gap: 20px;
}

.text {
  margin-bottom: 20px;

  font-size: 20px;
  color: var(--warning-color);
}
</style>
