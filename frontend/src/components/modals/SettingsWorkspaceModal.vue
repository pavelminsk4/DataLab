<template>
  <BaseModal>
    <section>
      <div class="title">Settings</div>

      <div class="settings-options">
        <div
          v-for="(item, index) in buttons"
          :key="'button' + index"
          @click="openSettings"
          :class="[
            'option',
            settingName === item.name && 'option option-active',
          ]"
        >
          {{ item.name }}
        </div>
      </div>

      <section class="form-sections">
        <div v-if="settingName === 'General'" class="settings-wrapper">
          <BaseInput
            v-model.trim="title"
            label="Workspace name"
            :is-settings="true"
            :hasError="!!titleError"
            :errorMessage="titleError"
            class="form-title"
            @blur="validation"
          />

          <div class="form-title">Workspace description</div>

          <BaseTextarea v-model="description" placeholder="Description" />
        </div>

        <div v-if="settingName === 'Permissions'" class="permissions-wrapper">
          <div class="form-title">Owner</div>
        </div>

        <BaseButton @click="saveSettings" class="button"> Save </BaseButton>
      </section>
    </section>
  </BaseModal>
</template>

<script>
import BaseModal from '@components/modals/BaseModal'
import BaseInput from '@/components/common/BaseInput'
import BaseButton from '@/components/common/BaseButton'
import BaseTextarea from '@/components/common/BaseTextarea'

export default {
  name: 'SettingsWorkspaceModal',
  components: {
    BaseButton,
    BaseInput,
    BaseModal,
    BaseTextarea,
  },
  data() {
    return {
      loading: false,
      newTitle: null,
      titleError: null,
      newDescription: null,
      settingName: 'General',
      buttons: [{name: 'General'}, {name: 'Permissions'}],
    }
  },
  props: {
    member: {
      type: [Number, String],
      default: '',
    },
    currentWorkspace: {
      type: Object,
      required: true,
    },
  },
  computed: {
    members() {
      let members = []
      members.push(this.member)
      return members
    },
    title: {
      get() {
        if (this.newTitle === '') return this.newTitle
        return this.newTitle || this.currentWorkspace.title
      },
      set(val) {
        this.newTitle = val
        this.titleError = null
      },
    },
    description: {
      get() {
        if (this.newDescription === '') return this.newDescription
        return this.newDescription || this.currentWorkspace.description || ''
      },
      set(val) {
        this.newDescription = val
      },
    },
  },
  methods: {
    openSettings(e) {
      this.settingName =
        this.settingName === e.target.innerText ? 'General' : e.target.innerText
    },
    saveSettings() {
      if (this.titleError) return
      this.$emit('save-settings', this.title, this.description)
    },
    validation() {
      this.titleError = this.title ? null : 'required'
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 25px;

  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
  color: var(--typography-primary-color);
}

.settings-options {
  display: flex;

  border-bottom: 1px solid var(--input-border-color);

  .option {
    cursor: pointer;

    padding-bottom: 12px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;
    color: rgba(255, 255, 255, 0.8);

    &:first-child {
      margin-right: 25px;
    }
  }

  .option-active {
    border-bottom: 1px solid var(--button-primary-color);

    color: var(--typography-primary-color);
  }
}

.form-sections {
  display: flex;
  flex-direction: column;

  margin-top: 25px;

  .form-title {
    margin: 20px 0 12px 0;

    font-weight: 500;
    font-size: 14px;
    line-height: 110%;
    color: var(--typography-primary-color);
  }

  .button {
    align-self: flex-end;

    margin-top: 20px;
    width: 103px;
  }
}
</style>
