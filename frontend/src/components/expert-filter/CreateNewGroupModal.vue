<template>
  <BaseModal style="--base-modal-content-padding: 0">
    <template #title>
      <span>Save as</span>
    </template>

    <section class="form">
      <BaseInput
        v-model="name"
        label="Group Name"
        placeholder="Enter group name"
      />

      <BaseTextarea
        v-model="description"
        placeholder="Some words about group"
        label="Description"
      />
    </section>

    <footer class="footer">
      <BaseButton :is-disabled="isDisabledSaveButton">
        <SaveIcon />
        <span>Save preset</span>
      </BaseButton>
    </footer>
  </BaseModal>
</template>

<script>
import BaseButton from '@/components/common/BaseButton'
import BaseModal from '@/components/modals/BaseModal'
import BaseInput from '@components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import SaveIcon from '@components/icons/SaveIcon'

export default {
  name: 'CreateNewGroupModal',
  components: {
    BaseButton,
    BaseModal,
    BaseInput,
    BaseTextarea,
    SaveIcon,
  },
  data() {
    return {
      newName: '',
      newDescription: '',
    }
  },
  computed: {
    name: {
      get() {
        return this.newName
      },
      set(val) {
        this.newName = val
      },
    },
    description: {
      get() {
        return this.newDescription
      },
      set(val) {
        this.newDescription = val
      },
    },
    isDisabledSaveButton() {
      return !this.name
    },
  },
}
</script>

<style lang="scss" scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: 24px;

  min-width: 570px;
  padding: 24px 24px 40px 24px;
}

.footer {
  display: flex;
  justify-content: flex-end;

  width: 100%;
  padding: 18px 24px;
  gap: 16px;

  background-color: var(--background-secondary-color);
  border-top: var(--border-primary);
}
</style>
