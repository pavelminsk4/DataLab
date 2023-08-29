<template>
  <BaseModal style="--base-modal-content-padding: 0">
    <template #title>
      <span>Create new group</span>
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
      <BaseButton :is-disabled="isDisabledSaveButton" @click="createGroup">
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
import BaseTextarea from '@/components/common/BaseTextarea'
import SaveIcon from '@components/icons/SaveIcon'

const {mapActions} = createNamespacedHelpers('expertFilter')

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
    ...mapGetters({user: get.USER_INFO}),
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
  methods: {
    ...mapActions([
      action.CREATE_PRESETS_GROUP,
      action.DELETE_PRESETS_GROUP,
      action.UPDATE_PRESETS_GROUP,
    ]),
    async createGroup() {
      await this[action.CREATE_PRESETS_GROUP]({
        data: {
          creator: this.user.id,
          title: this.name,
          description: this.description,
        },
      })
      this.$emit('close', this.name)
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
