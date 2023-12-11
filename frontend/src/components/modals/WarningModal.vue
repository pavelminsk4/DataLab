<template>
  <BaseModal modal-frame-style="width:456px;">
    <template #title>
      <CustomText text="Save confirmation" tag="div" />
    </template>

    <div class="warning-content">
      <img src="@assets/warning.svg" alt="Warning" class="warning-img" />

      <div class="text-container">
        <slot></slot>
      </div>
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
.warning-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 28px;

  margin-bottom: 28px;

  .warning-img {
    width: 315px;
  }
}

.text-container {
  display: flex;
  flex-direction: column;

  width: 100%;

  & > * {
    margin: 0;
    color: var(--typography-title-color);
  }
}

.modal-buttons {
  display: flex;

  gap: 20px;

  justify-content: flex-end;
}
</style>
