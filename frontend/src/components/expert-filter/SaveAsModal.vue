<template>
  <BaseModal style="--base-modal-content-padding: 0">
    <template #title>
      <span>Save as</span>
    </template>

    <section class="save-form">
      <BaseInput v-model="name" label="Name" placeholder="Enter preset name" />

      <BaseSelect
        v-model="selectedGroup"
        select-title="Group"
        placeholder="Select group"
        :options="options"
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
import BaseSelect from '@components/BaseSelect'
import SaveIcon from '@components/icons/SaveIcon'

export default {
  name: 'SaveAsModal',
  components: {
    BaseButton,
    BaseModal,
    BaseInput,
    BaseSelect,
    SaveIcon,
  },
  props: {
    currentName: {type: String, default: ''},
    currentSelectedGroup: {type: String, default: ''},
    options: {type: Array, default: () => []},
  },
  data() {
    return {
      newName: null,
      newSelectedGroup: null,
    }
  },
  computed: {
    name: {
      get() {
        return typeof this.newName === 'string'
          ? this.newName
          : this.currentName
      },
      set(val) {
        this.newName = val
      },
    },
    selectedGroup: {
      get() {
        return this.newSelectedGroup || this.currentSelectedGroup
      },
      set(val) {
        this.newSelectedGroup = val
      },
    },
    isDisabledSaveButton() {
      return !this.name || !this.isDisableSaveButton
    },
  },
}
</script>

<style lang="scss" scoped>
.save-form {
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
