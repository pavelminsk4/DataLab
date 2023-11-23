<template>
  <BaseModal modal-frame-style="width:456px;">
    <template #title>
      <CustomText tag="div">Save confirmation</CustomText>
    </template>

    <div class="warning-content">
      <img src="@assets/warning.svg" alt="Warning" class="warning-img" />

      <CustomText tag="div" class="text">
        After clicking the 'Continue' button, you will not be able to edit the
        project settings. <br />
        Please make sure that the keywords entered are correct.
      </CustomText>
    </div>

    <div class="modal-buttons">
      <BaseButton :is-not-background="true" @click="$emit('close')">
        <CustomText text="Cancel" />
      </BaseButton>
      <BaseButton @click.stop="$emit('approve')">
        <CustomText text="Continue" />
      </BaseButton>
    </div>
  </BaseModal>
</template>

<script>
import CustomText from '@components/CustomText'
import BaseButton from '@components/common/BaseButton'
import BaseModal from '@components/modals/BaseModal'

export default {
  name: 'WarningModal',
  components: {BaseModal, BaseButton, CustomText},
}
</script>

<style lang="scss">
.modal-buttons {
  display: flex;
  gap: 20px;

  justify-content: flex-end;
}

.text {
  margin-bottom: 20px;

  color: var(--typography-title-color);
}

.warning-content {
  display: flex;
  flex-direction: column;
  align-items: center;

  .warning-img {
    width: 315px;
    margin-bottom: 28px;
  }
}
</style>
