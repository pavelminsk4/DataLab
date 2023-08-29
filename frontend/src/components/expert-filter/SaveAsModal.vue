<template>
  <BaseModal
    :is-overflow-visible="true"
    style="--base-modal-content-padding: 0"
  >
    <template #title>
      <span>Save as</span>
    </template>

    <CreateNewGroupModal
      v-if="isOpenCreateGroupModal"
      @close="closeGroupModal"
    />
    <PresetCreatedModal v-if="isOpenAlertModal" @close="$emit('close')" />

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
        <li v-for="{id, title} in groups" :key="id" @click="slotProps.select">
          {{ title }}
        </li>

        <button class="create-group-btn" @click="isOpenCreateGroupModal = true">
          <PlusIcon />
          <span>Create new group</span>
        </button>
      </BaseSelect>
    </section>

    <footer class="footer">
      <BaseButton :is-disabled="isDisabledSaveButton" @click="createPreset">
        <SaveIcon color="#ffffff" />
        <span>Save preset</span>
      </BaseButton>
    </footer>
  </BaseModal>
</template>

<script>
import {createNamespacedHelpers, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/common/BaseButton'
import BaseModal from '@/components/modals/BaseModal'
import BaseInput from '@components/common/BaseInput'
import BaseSelect from '@components/BaseSelect2'
import CreateNewGroupModal from '@/components/expert-filter/CreateNewGroupModal'
import PresetCreatedModal from '@/components/expert-filter/PresetCreatedModal'

import SaveIcon from '@components/icons/SaveIcon'
import PlusIcon from '@components/icons/PlusIcon.vue'

const {mapActions, mapGetters: mapExpertFilterGetters} =
  createNamespacedHelpers('expertFilter')

export default {
  name: 'SaveAsModal',
  components: {
    BaseButton,
    BaseModal,
    BaseInput,
    BaseSelect,
    CreateNewGroupModal,
    PresetCreatedModal,
    SaveIcon,
    PlusIcon,
  },
  props: {
    expertQuery: {type: String, required: true},
  },
  data() {
    return {
      newName: null,
      newSelectedGroup: null,
      isOpenCreateGroupModal: false,
      isOpenAlertModal: false,
    }
  },
  computed: {
    ...mapGetters({user: get.USER_INFO}),
    ...mapExpertFilterGetters({groups: get.PRESET_GROUPS}),
    name: {
      get() {
        return typeof this.newName === 'string' ? this.newName : ''
      },
      set(val) {
        this.newName = val
      },
    },
    selectedGroup: {
      get() {
        return this.newSelectedGroup || ''
      },
      set(val) {
        this.newSelectedGroup = val
      },
    },
    selectedGroupData() {
      return this.groups.find(({title}) => this.selectedGroup === title)
    },
    isDisabledSaveButton() {
      return !this.name || !this.selectedGroupData?.id
    },
  },
  methods: {
    ...mapActions([action.CREATE_PRESET]),
    async createPreset() {
      console.log('CREATE PR', this.selectedGroupData)
      await this[action.CREATE_PRESET]({
        data: {
          title: this.name,
          group: this.selectedGroupData.id,
          query: this.expertQuery,
          creator: this.user.id,
        },
      })

      this.isOpenAlertModal = true
    },
    closeGroupModal(groupName) {
      this.isOpenCreateGroupModal = false
      if (!groupName) return
      this.selectedGroup = groupName
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
