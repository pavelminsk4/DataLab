<template>
  <BaseModal
    :is-overflow-visible="true"
    style="--base-modal-content-padding: 0"
  >
    <template #title>
      <span>Save as</span>
    </template>

    <section class="save-form">
      <BaseInput v-model="name" label="Name" placeholder="Enter preset name" />

      <BaseSelect
        v-model="selectedGroup"
        v-slot="slotProps"
        selectName="group"
        select-title="Group"
        placeholder="Select group"
        style="--options-container-height: 180px"
      >
        <li v-for="{id, name} in groups" :key="id" @click="slotProps.select">
          {{ name }}
        </li>

        <button class="create-group-btn" @click="createGroup">
          <PlusIcon />
          <span>Create new group</span>
        </button>
      </BaseSelect>
    </section>

    <footer class="footer">
      <BaseButton :is-disabled="isDisabledSaveButton">
        <SaveIcon color="#ffffff" />
        <span>Save preset</span>
      </BaseButton>
    </footer>
  </BaseModal>
</template>

<script>
import BaseButton from '@/components/common/BaseButton'
import BaseModal from '@/components/modals/BaseModal'
import BaseInput from '@components/common/BaseInput'
import BaseSelect from '@components/BaseSelect2'
import SaveIcon from '@components/icons/SaveIcon'
import PlusIcon from '@components/icons/PlusIcon.vue'

export default {
  name: 'SaveAsModal',
  components: {
    BaseButton,
    BaseModal,
    BaseInput,
    BaseSelect,
    SaveIcon,
    PlusIcon,
  },
  props: {
    currentName: {type: String, default: ''},
    currentSelectedGroup: {type: String, default: ''},
    groups: {
      type: Array,
      default: () => [
        {id: 2, name: 'Name name1'},
        {id: 24, name: 'Name name2'},
        {id: 4, name: 'Name name3'},
        {id: 43, name: 'Name name4'},
        {id: 44, name: 'Name name5'},
        {id: 45, name: 'Name name'},
        {id: 454, name: 'Name name'},
        {id: 452, name: 'Name name'},
        {id: 451, name: 'Name name'},
        {id: 455, name: 'Name name'},
        {id: 456, name: 'Name name'},
      ],
    },
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
        return this.newSelectedGroup || this.currentSelectedGroup || ''
      },
      set(val) {
        this.newSelectedGroup = val
      },
    },
    isDisabledSaveButton() {
      return !this.name || !this.isDisableSaveButton
    },
  },
  methods: {
    createGroup() {
      console.log('CREATE GROUP')
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

.create-group-btn {
  position: sticky;
  bottom: -15;

  display: flex;
  align-items: center;
  gap: 10px;

  margin: 0 -15px -15px;
  padding: 12px;

  background-color: var(--background-secondary-color);
  border: none;
  border-radius: var(--border-radius);
  box-shadow: 2px 2px 8px 0px rgba(135, 135, 135, 0.2),
    -2px -6px 4px 0px rgba(135, 135, 135, 0.05);

  cursor: pointer;

  svg {
    color: var(--primary-color);
  }
}
</style>
