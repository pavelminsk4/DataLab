<template>
  <BaseModal modal-frame-style="width:456px;">
    <template #title>
      <CustomText text="Save confirmation" tag="div" />
    </template>

    <div class="warning-content">
      <img src="@assets/warning.svg" alt="Warning" class="warning-img" />

      <CustomText
        tag="div"
        text="After clicking the 'Continue' button, you will not be able to edit the
        project settings."
        class="text"
      />
      <CustomText
        tag="div"
        text="Please make sure that the keywords entered are correct."
        class="text"
      />
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
  display: flex;
  align-self: flex-start;

  color: var(--typography-title-color);
}

.warning-content {
  display: flex;
  flex-direction: column;
  align-items: center;

  margin-bottom: 28px;

  .warning-img {
    width: 315px;
    margin-bottom: 28px;
  }
}
</style>
